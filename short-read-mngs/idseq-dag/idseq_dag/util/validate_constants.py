READ_LEN_CUTOFF_LOW = 50
READ_LEN_CUTOFF_MID = 500
READ_LEN_CUTOFF_HIGH = 10000
# Maximum allowed line length in characters for fastq/fasta files
MAX_LINE_LENGTH = READ_LEN_CUTOFF_HIGH

BUCKET_TOO_SHORT = f"<{READ_LEN_CUTOFF_LOW}"
BUCKET_NORMAL = f"{READ_LEN_CUTOFF_LOW}-{READ_LEN_CUTOFF_MID}"
BUCKET_LONG = f"{READ_LEN_CUTOFF_MID}-{READ_LEN_CUTOFF_HIGH}"
BUCKET_TOO_LONG = f"{READ_LEN_CUTOFF_HIGH}+"
