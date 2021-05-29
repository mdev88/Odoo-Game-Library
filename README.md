# Odoo Game Library

Odoo add-on to manage a simple game library.

I created this add-on just to practice Odoo modules development, so don't expect much :)

This was developed with Odoo 13 Community in mind, and I have not tested it in any other version yet.

## Dependencies

This module needs the python package rawgpy.

I am running Odoo from the official Docker image, so in my caso what I did is:

```shell
# Go into the Odoo container
docker exec -u root -it docker_web_1 /bin/bash
```

And then restart the container to reflect the new changes.
