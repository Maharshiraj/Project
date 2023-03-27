import shutil
from rest_framework import serializers
from .models import *


class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = myFiles
        fields = '__all__'

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
    )
    folder = serializers.CharField(required = False)
    
    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,f'public/static/{folder}' )
        #..........(TARGET LOCATION for zipped folder, zip this selected folder ,SOURCE LOCATION to select which folder to zip)

    def create(self , validated_data):
        new_Folder = myFolder.objects.create()
        new_Files = validated_data.pop('files')
        files_objs = []
        for newfile in new_Files:
            files_obj = myFiles.objects.create(folder = new_Folder , file = newfile)
            files_objs.append(files_obj)

        
        self.zip_files(new_Folder.uid)


        return {'files' : {} , 'folder' : str(new_Folder.uid)}