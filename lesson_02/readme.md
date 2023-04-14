# Edit your page using git and vscode

## Download vscode
https://code.visualstudio.com/download

## Setup Git
> Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows - [Wikipedia](https://en.wikipedia.org/wiki/Git)

### Create ssh key
This allows you to make changes without needing to log into Github for every change

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Add to github
```bash
 cat ~/.ssh/id_ed25519.pub
```
https://github.com/settings/keys


### Clone (download) repo(sitory)
```bash
git clone git@github.com:<username>/<username>.github.io.git
```

## Edit file

### Open folder
```bash
cd <username>.github.io.git
code . # opens folder in vscode
```

###  Edit
Make any changes you want

## See changes locally before pushing to the internet

You can Add vscode extension [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) to keep things running locally. Or if you want to test something on the internet so you can see it from another computer or phone use [telebit](https://telebit.cloud/). Note: Remember to run `telebit disable` when you are done using it to not leave a port open for hackers to attack your computer.

## Save changes

* Look in vscode under the `Source Control` tab to see changes
* Add those changes
    * Alternatively type `git add .` where `.`(dot) means all changes in the folder.
* Click `Commit` to save the gropu of changes together with a name
    * Alternatively type `git commit -m "<message of changes>"`
* `Push` or `Sync` to save the changes to the internet
    * Alternatively type `git push origin HEAD`


## Notes

List of helpful git commands
https://gist.github.com/mvndaai/86dab188665d2f8ac4eff9ab16c48199

* Seeing what changes exist
    * To setup an alias of for a more user friendly `git log`run 
    ```bash
    git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold yellow)<%an>%Creset' --abbrev-commit"
    ```
    * Type `git lg`
        * Anything that starts with `origin/` is in the internet.
        * `HEAD` is where your computer is currently looking at

* If you don't want vscode installed locally you can change the github website from `.com` to `.dev` to edit through their webiste
