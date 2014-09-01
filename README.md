Setup
-----
To run this project with Vagrant, run the following commands in project folder:

    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/



If you dont want to use Vagrant to run this project, than look at the `etc/install/install.sh` for details about how to setupthe project.
Most likely after setting Database credentials in shopin/settings/base.py you will need to do following:

    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py loaddata etc/fixtures/core.json"
