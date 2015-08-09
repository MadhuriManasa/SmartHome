#!/usr/bin/env python3

# Copyright (c) 2015 ObjectLabs Corporation
# Distributed under the MIT license - http://opensource.org/licenses/MIT

from pymongo import MongoClient  # pymongo>=3.0

"""
PyMongo Production Connection Example
The following example uses PyMongo to connect to a MongoDB deployment using the options we have found most appropriate to
production applications. This example supports both replica set and SSL connections.
For demonstration purposes, configuration is hard-coded; in practice, configuration should be externalized e.g. into a file or
environment variables.
  ##########################################################################################################################
  WARNING: This example requires PyMongo 3.0 or later to work correctly. In particular, if you are connecting over SSL
           with an earlier driver version additional configuration will be required for it to properly authenticate the
           server.
  ##########################################################################################################################
"""

# Your deployment's URI in the standard format (http://docs.mongodb.org/manual/reference/connection-string/).
#
# The URI can be found via the MongoLab management portal (http://docs.mongolab.com/connecting/#connect-string).
#
# If you are using a PaaS add-on integration e.g. via Heroku, the URI is usually available via an environment variable, often
# named "MONGOLAB_URI". Consult the documentation for the add-on you are using.
mongolab_uri = "mongodb://bharath2020:bharathmongo@ds031223.mongolab.com:31223/heroku_9g9jq5mx"

# Pass the following keyword arguments to ensure proper production behavior:
#
#   connectTimeoutMS  30 s to allow for PaaS warm-up; adjust down as needed for faster failures. For more, see docs:
#                     http://docs.mongolab.com/timeouts/#connection-timeout
#
#   socketTimeoutMS   No timeout (None) to allow for long-running operations
#                     (http://docs.mongolab.com/timeouts/#socket-timeout).
#
#   socketKeepAlive   Enabled (True) to ensure idle connections are kept alive in the presence of a firewall.
#
# See PyMongo docs for more details about the connection options:
#
#   https://api.mongodb.org/python/3.0/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
#


class SmartHomeDB:

	def __init__(self):
		self.client = client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None)
		self.db = client.get_default_database()
		self.temperature_collection = self.db['temperature']

	def getTemperaturePoints(self):
		record = self.temperature_collection.find({},{'temperature':1,'humidity':1,'device_name':1,'_id':0})
		return list(record)

	def insertTemperaturePoint(self,tempData):
		record = {};
		record['temperature'] = tempData['temperature']
		record['humidity'] = tempData['humidity'];
		record['timestamp'] = tempData['timestamp']
		record['device_name'] = tempData['device_name']
		self.temperature_collection.insert_one(record)






