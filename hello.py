#!/usr/bin/env python3

import os
import json
env_vars = {key:val for key,val in os.environ.items()}
print("Content-Type: text/json\n")    # HTML is following
print(json.dumps(env_vars))  