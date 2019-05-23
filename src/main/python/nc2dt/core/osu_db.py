from struct import unpack_from, calcsize
from ..utils import debug
from collections import namedtuple
from pathlib import Path
import os
import time

def get_default_osu_path():
    local_app_data = Path(os.getenv("LOCALAPPDATA"))
    osu_path = local_app_data / Path('osu!')
    if not osu_path.exists():
        raise RuntimeError("Couldn't find osu! installation folder.")
    
    return osu_path

class OsuDBReader(object):
    def __init__(self, contents):
        self.contents = contents
        self.pos = 0
        debug("OsuDBReader: length: {}".format(len(contents)))
    

    def _read(self, value_type):
        value = unpack_from(value_type, self.contents, self.pos)[0]
        self.pos += calcsize(value_type)
        return value
    

    def skip(self, length):
        self.pos += length
    

    def read_byte(self):
        return self._read('b')
    

    def read_boolean(self):
        return self.read_byte() != 0x00


    def read_short(self):
        return self._read('h')
    

    def read_int(self):
        return self._read('i')
    

    def read_long(self):
        return self._read('q')
    

    def read_uleb128(self):
        result = 0
        shift = 0
        while True:
            value = self._read('B')
            result |= (value & 0x7F) << shift
            if (value & 0x80) == 0:
                break
            shift += 7
        return result
    

    def read_string(self):
        not_empty = self.read_boolean()
        if not not_empty:
            return ''
        
        length = self.read_uleb128()
        try:
            return self._read(str(length) + 's').decode('utf-8')
        except UnicodeDecodeError:
            debug("OsuDBReader.read_string: failed to decode UTF-8 string, returning empty string")
            return ""
    

    def skip_string(self):
        not_empty = self.read_boolean()
        if not not_empty:
            return ''
        
        length = self.read_uleb128()
        self.skip(length)


Beatmap = namedtuple("Beatmap", ["artist", "title", "creator", "difficulty", "audio", "folder_name"])


class OsuDB(object):
    def __init__(self, db_path: Path):
        self.version = 0
        self.user = ""
        self.beatmaps = []
        
        debug("OsuDB: Reading osu!.db file")
        start = time.time()
        self._read(db_path)
        end = time.time()
        debug("OsuDB: Finished reading in", end - start, "seconds")
    
    def _skip_diff_pairs(self, db_reader: OsuDBReader):
        pairs_count = db_reader.read_int()
        db_reader.skip(14 * pairs_count)
    
    def _skip_timing_points(self, db_reader: OsuDBReader):
        timings_count = db_reader.read_int()
        db_reader.skip(17 * timings_count)

    def _read_beatmap(self, db_reader: OsuDBReader):
        expected_finish = db_reader.read_int() + db_reader.pos
        
        artist = db_reader.read_string()
        db_reader.skip_string() # Artist (Unicode)
        title = db_reader.read_string()
        db_reader.skip_string() # Title (Unicode)
        creator = db_reader.read_string()
        difficulty = db_reader.read_string()
        audio = db_reader.read_string()

        debug("Beatmap details: {} - {} ({}) [{}]; audio: {}".format(artist, title, creator, difficulty, audio))
        db_reader.skip_string() # MD5 hash
        db_reader.skip_string() # .osu location
        db_reader.skip(1) # Ranked status
        db_reader.skip(2 * 3) # Hitcircles/sliders/spinners
        db_reader.skip(8) # Last modification time
        if self.version < 20140609: # AR/CS/HP/OD
            db_reader.skip(1 * 4)
        else:
            db_reader.skip(4 * 4)
        
        db_reader.skip(8) # SV
        if self.version >= 20140609:
            self._skip_diff_pairs(db_reader) # osu!std
            self._skip_diff_pairs(db_reader) # taiko
            self._skip_diff_pairs(db_reader) # CTB
            self._skip_diff_pairs(db_reader) # mania
        db_reader.skip(4 * 3) # Drain time/Total time/Preview
        self._skip_timing_points(db_reader)
        db_reader.skip(4 * 3) # Beatmap ID/Beatmap set ID/Thread ID
        db_reader.skip(1 * 4) # Grade in all 4 modes
        db_reader.skip(2) # Local offset
        db_reader.skip(4) # Stack leniency
        db_reader.skip(1) # Mode
        db_reader.skip_string() # Song source
        db_reader.skip_string() # Tags
        db_reader.skip(2) # Online offset
        db_reader.skip_string() # Font used for the title
        db_reader.skip(1) # Unplayed (bool)
        db_reader.skip(8) # Last played
        db_reader.skip(1) # osz2? (bool)
        
        folder_name = db_reader.read_string()
        db_reader.skip(8) # Last time checked against osu! repo
        db_reader.skip(1 * 5) # Ignore sounds/skin/storyboard/video/visual override
        if self.version < 20140609:
            db_reader.skip(2) # not even osu wiki knows
        db_reader.skip(4) # Last modification time
        db_reader.skip(1) # Mania scroll speed

        if db_reader.pos != expected_finish:
            debug("OsuDB._read_beatmap: Didn't reach expected position after processing beatmap. Corrupted?")
            db_reader.pos = expected_finish
            return None
        
        return Beatmap(artist, title, creator, difficulty, audio, folder_name)

    def _read(self, db_path):
        with open(db_path, "rb") as f:
            db_reader = OsuDBReader(f.read())
            self.version = db_reader.read_int()
            # Skip Folder Count, AccountUnlocked and a DateTime
            db_reader.skip(4 + 1 + 8)
            self.user = db_reader.read_string()
            beatmap_count = db_reader.read_int()

            debug("OsuDB._read: Reading {}'s osu!.db (version {}). Expecting {} beatmaps.".format(self.user, self.version, beatmap_count))

            for i in range(beatmap_count):
                beatmap = self._read_beatmap(db_reader)
                if beatmap is not None:
                    self.beatmaps.append(beatmap)
            
            debug("OsuDB._read: Finished. Read {} out of {} beatmaps.".format(len(self.beatmaps), beatmap_count))

    def search_beatmap(self, text):
        def _beatmap_match(beatmap: Beatmap):
            return all([
                any([
                    word.lower() in field.lower()
                    for field in beatmap._asdict().values()
                ])
                for word in text.split()
            ])
        return list(filter(_beatmap_match, self.beatmaps))

