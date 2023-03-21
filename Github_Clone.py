import git

def git_clone():
    return  git.Repo.clone_from("https://github.com/PhonePe/pulse.git", "PhonePe_Pulse")

if __name__ == "__main__":
    
    git_clone()
    

