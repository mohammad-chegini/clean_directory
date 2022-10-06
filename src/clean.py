import shutil
from pathlib import Path
from loguru import logger

class OrganizeFiles:
    def __init__(self,directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f'{self.directory} does not exist')

        self.file_type_dest = {
            '.jpeg':'IMAGE',
            '.pdf' :'DATA',
            '.doc' :'DATA',
            '.txt' :'DATA',
            '.zip' :'COMPRESS',
            '.rar' :'COMPRESS',
            '.jpg' :'IMAGE',
            '.json':'DATA',
            '.docx':'DATA',
            '.dxf' :'DATA',
        '.apk' :'APPLICATION',
        }
    
    def __call__(self):
        file_extension=[]

        for file_path in self.directory.iterdir():
            if file_path.is_dir():
                continue
            file_extension.append(file_path.suffix)
    
            if file_path.suffix not in self.file_type_dest:
                DEST_DIR=self.directory/'OTHER'
            else:
                DEST_DIR = self.directory / self.file_type_dest[file_path.suffix]

            DEST_DIR.mkdir(exist_ok=True)
            logger.info(f"Moving{file_path.suffix:10} to {DEST_DIR}")
            shutil.move(str(file_path),str(DEST_DIR))
            

if __name__ == "__main__":
    org_file = OrganizeFiles('/mnt/c/Users/admin/Downloads')
    print('Done...')
    org_file()




