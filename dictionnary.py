"""
    This file contains the dictionnary that contains the path of the folder based on the extension of the file
"""

# Documents
DOCUMENT_PATH = "document/"
SPREADSHEET_PATH = "spreadsheet/"
PDF_PATH = "pdf/"
PRESENTATION_PATH = "presentation/"
TEXT_PATH = "text/"

# Media
MEDIA_PATH = "media/"
AUDIO_PATH = "audio/"
VIDEO_PATH = "video/"
IMAGE_PATH = "images/"

# Code
CODE_PATH = "code/"
PYTHON_PATH = "python/"
JAVA_PATH = "java/"
C_PATH = "c/"
H_PATH = "h/"
CPP_PATH = "cpp/"
HTML_PATH = "html/"
CSS_PATH = "css/"
JS_PATH = "js/"
PHP_PATH = "php/"
SQL_PATH = "sql/"
MD_PATH = "md/"
R_PATH = "r/"
GO_PATH = "go/"
SWIFT_PATH = "swift/"
KOTLIN_PATH = "kotlin/"
RUBY_PATH = "ruby/"
PERL_PATH = "perl/"
RUST_PATH = "rust/"

# Data
DATA_PATH = "data/"
CSV_PATH = "csv/"
JSON_PATH = "json/"
XML_PATH = "xml/"

# Archive
ARCHIVE_PATH = "archive/"
ZIP_PATH = "zip/"
TAR_PATH = "tar/"
GZ_PATH = "gz/"
RAR_PATH = "rar/"
SEVENZ_PATH = "7z/"
BZ2_PATH = "bz2/"
XZ_PATH = "xz/"
DEB_PATH = "deb/"
RPM_PATH = "rpm/"
ISO_PATH = "iso/"
IMG_PATH = "img/"
DMG_PATH = "dmg/"

# Executable
EXECUTABLE_PATH = "executable/"
EXE_PATH = "exe/"
BIN_PATH = "bin/"
SH_PATH = "sh/"
BAT_PATH = "bat/"
PS1_PATH = "ps1/"
PYC_PATH = "pyc/"
CLASS_PATH = "class/"
JAR_PATH = "jar/"
WAR_PATH = "war/"

# Font
FONT_PATH = "font/"
TTF_PATH = "ttf/"
OTF_PATH = "otf/"
FON_PATH = "fon/"
FNT_PATH = "fnt/"

# System
SYSTEM_PATH = "system/"
DLL_PATH = "dll/"
SYS_PATH = "sys/"
CFG_PATH = "cfg/"
INI_PATH = "ini/"
LOG_PATH = "log/"
TMP_PATH = "tmp/"
TEMP_PATH = "temp/"
BAK_PATH = "bak/"

# Other
OTHER_PATH = "other/"
TORRENT_PATH = "torrent/"

"""
    Dictionnary that contains the path of the folder based on the extension of the file
"""
path_based_on_extension = {
    # Images
    "jpg": MEDIA_PATH + IMAGE_PATH + "jpg",
    "jpeg":  MEDIA_PATH + IMAGE_PATH + "jpeg",
    "png": MEDIA_PATH + IMAGE_PATH + "png",
    "gif": MEDIA_PATH + IMAGE_PATH + "gif",
    "svg": MEDIA_PATH + IMAGE_PATH + "svg",
    "bmp": MEDIA_PATH + IMAGE_PATH + "bmp",
    "tiff": MEDIA_PATH + IMAGE_PATH + "tiff",
    "webp": MEDIA_PATH + IMAGE_PATH + "webp",
    # Audio
    "mp3": MEDIA_PATH + AUDIO_PATH + "mp3",
    "wav": MEDIA_PATH + AUDIO_PATH + "wav",
    "flac": MEDIA_PATH + AUDIO_PATH + "flac",
    "ogg": MEDIA_PATH + AUDIO_PATH + "ogg",
    "wma": MEDIA_PATH + AUDIO_PATH + "wma",
    "aac": MEDIA_PATH + AUDIO_PATH + "aac",
    "m4a": MEDIA_PATH + AUDIO_PATH + "m4a",
    "aiff": MEDIA_PATH + AUDIO_PATH + "aiff",
    "alac": MEDIA_PATH + AUDIO_PATH + "alac",
    "ape": MEDIA_PATH + AUDIO_PATH + "ape",
    "dsd": MEDIA_PATH + AUDIO_PATH + "dsd",
    "mpc": MEDIA_PATH + AUDIO_PATH + "mpc",
    # Video
    "mp4": MEDIA_PATH + VIDEO_PATH + "mp4",
    "avi": MEDIA_PATH + VIDEO_PATH + "avi",
    "mkv": MEDIA_PATH + VIDEO_PATH + "mkv",
    "mov": MEDIA_PATH + VIDEO_PATH + "mov",
    "wmv": MEDIA_PATH + VIDEO_PATH + "wmv",
    "flv": MEDIA_PATH + VIDEO_PATH + "flv",
    "webm": MEDIA_PATH + VIDEO_PATH + "webm",
    "vob": MEDIA_PATH + VIDEO_PATH + "vob",
    "3gp": MEDIA_PATH + VIDEO_PATH + "3gp",
    "mpg": MEDIA_PATH + VIDEO_PATH + "mpg",
    "mpeg": MEDIA_PATH + VIDEO_PATH + "mpeg",
    "m4v": MEDIA_PATH + VIDEO_PATH + "m4v",
    "rmvb": MEDIA_PATH + VIDEO_PATH + "rmvb",
    "webm": MEDIA_PATH + VIDEO_PATH + "webm",
    # Documents
    "doc": DOCUMENT_PATH + TEXT_PATH + "doc",
    "docx": DOCUMENT_PATH + TEXT_PATH + "docx",
    "odt": DOCUMENT_PATH + TEXT_PATH + "odt",
    "pdf": DOCUMENT_PATH + PDF_PATH + "pdf",
    "xls": DOCUMENT_PATH + SPREADSHEET_PATH + "xls",
    "xlsx": DOCUMENT_PATH + SPREADSHEET_PATH + "xlsx",
    "xlsm": DOCUMENT_PATH + SPREADSHEET_PATH + "xlsm",
    "ppt": DOCUMENT_PATH + PRESENTATION_PATH + "ppt",
    "pptx": DOCUMENT_PATH + PRESENTATION_PATH + "pptx",
    "odp": DOCUMENT_PATH + PRESENTATION_PATH + "odp",
    "txt": DOCUMENT_PATH + TEXT_PATH + "txt",
    "rtf": DOCUMENT_PATH + TEXT_PATH + "rtf",
    # Code
    "py": CODE_PATH + PYTHON_PATH ,
    "java": CODE_PATH + JAVA_PATH ,
    "c": CODE_PATH + C_PATH,
    "h": CODE_PATH + H_PATH,
    "cpp": CODE_PATH + CPP_PATH,
    "html": CODE_PATH + HTML_PATH,
    "css": CODE_PATH + CSS_PATH,
    "js": CODE_PATH + JS_PATH,
    "php": CODE_PATH + PHP_PATH,
    "sql": CODE_PATH + SQL_PATH,
    "md": CODE_PATH + MD_PATH,
    "r": CODE_PATH + R_PATH,
    "go": CODE_PATH + GO_PATH,
    "swift": CODE_PATH + SWIFT_PATH,
    "kotlin": CODE_PATH + KOTLIN_PATH,
    "ruby": CODE_PATH + RUBY_PATH,
    "perl": CODE_PATH + PERL_PATH,
    "rust": CODE_PATH + RUST_PATH,
    # Data
    "csv": DATA_PATH + CSV_PATH,
    "json": DATA_PATH + JSON_PATH,
    "xml": DATA_PATH + XML_PATH,
    # Archive
    "zip": ARCHIVE_PATH + ZIP_PATH,
    "tar": ARCHIVE_PATH + TAR_PATH,
    "gz": ARCHIVE_PATH + GZ_PATH,
    "rar": ARCHIVE_PATH + RAR_PATH,
    "7z": ARCHIVE_PATH + SEVENZ_PATH,
    "bz2": ARCHIVE_PATH + BZ2_PATH,
    "xz": ARCHIVE_PATH + XZ_PATH,
    "deb": ARCHIVE_PATH + DEB_PATH,
    "rpm": ARCHIVE_PATH + RPM_PATH,
    "iso": ARCHIVE_PATH + ISO_PATH,
    "img": ARCHIVE_PATH + IMG_PATH,
    "dmg": ARCHIVE_PATH + DMG_PATH,
    # Executable
    "exe": EXECUTABLE_PATH + EXE_PATH,
    "bin": EXECUTABLE_PATH + BIN_PATH,
    "sh": EXECUTABLE_PATH + SH_PATH,
    "bat": EXECUTABLE_PATH + BAT_PATH,
    "ps1": EXECUTABLE_PATH + PS1_PATH,
    "pyc": EXECUTABLE_PATH + PYC_PATH,
    "class": EXECUTABLE_PATH + CLASS_PATH,
    "jar": EXECUTABLE_PATH + JAR_PATH,
    "war": EXECUTABLE_PATH + WAR_PATH,
    # Font
    "ttf": FONT_PATH + TTF_PATH,
    "otf": FONT_PATH + OTF_PATH,
    "fon": FONT_PATH + FON_PATH,
    "fnt": FONT_PATH + FNT_PATH,
    # System
    "dll": SYSTEM_PATH + DLL_PATH,
    "sys": SYSTEM_PATH + SYS_PATH,
    "cfg": SYSTEM_PATH + CFG_PATH,
    "ini": SYSTEM_PATH + INI_PATH,
    "log": SYSTEM_PATH + LOG_PATH,
    "tmp": SYSTEM_PATH + TMP_PATH,
    "temp": SYSTEM_PATH + TEMP_PATH,
    "bak": SYSTEM_PATH + BAK_PATH,
    # Other
    "torrent": OTHER_PATH + TORRENT_PATH
}