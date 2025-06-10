import os

def get_files_info(working_directory, directory = None):
    try:
        if directory:
             real_directory: str = os.path.realpath(os.path.join(working_directory, directory)) #real path, not getting tricked by symlinks
        else:
            real_directory: str = os.path.realpath(working_directory)

        if not real_directory.startswith(os.path.realpath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        #We restrict the LLM to the working directory so it doen't wreck havoc

        if not os.path.isdir(real_directory):
            return f'Error: "{directory}" is not a directory'
        
        files = []
        for doc in os.listdir(real_directory):
            is_dir = os.path.isdir(os.path.join(real_directory, doc))
            size = os.path.getsize(os.path.join(real_directory, doc))
            files.append(f"- {doc}: file_size={size}, is_dir={is_dir}")
        return "\n".join(files)
    
    except Exception as e:
        return f"Error: {str(e)}"