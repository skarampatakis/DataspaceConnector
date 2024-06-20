#!/usr/bin/env python3
#
# Copyright 2020-2022 Fraunhofer Institute for Software and Systems Engineering
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from resourceapi import ResourceApi
from idsapi import IdsApi
import pprint
import sys

provider_url = "http://service-provider:8484"
#consumer_url = "http://localhost:8383"
backend_url = "http://localhost:8585"
broker_url = "http://104.199.78.52:8282/infrastructure"


def main(argv):
    if len(argv) == 2:
        provider_url = argv[0]
      #  consumer_url = argv[1]
        print("Setting provider alias as:", provider_url)
      #  print("Setting consumer alias as:", consumer_url)


if __name__ == "__main__":
    main(sys.argv[1:])

print("Starting script")

# Provider
provider = ResourceApi(provider_url)

## Create resources
catalog = provider.create_catalog()
additional = {
    "https://www.trusts-data.eu/ontology/asset_type":
        "https://www.trusts-data.eu/ontology/" + "Service"}
offers = provider.create_offered_resource(data={
    "title":"Tweets Annotation Workflow - Review Demo",
    "description": "This is a test workflow to showcase how a service offer can look like.",
    "https://www.trusts-data.eu/ontology/asset_type": "https://www.trusts-data.eu/ontology/Service",
    "publisher":"http://publisher.com",
    "license": "http://license.com",
    "language":"EN"
}
)
representation_trigger = provider.create_representation(data={"title":"Service Gateway"})
representation_workflow = provider.create_representation(data={"title": "Workflow Definition"})
representation_output = provider.create_representation(data={"title": "Workflow Output"})
apiKey = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJpZ1ZTN01jNnFaQkx1aGFpeFV5S0dJVmN6d09mNVlyYzhONXNYODBPejlJIn0.eyJleHAiOjE3NDI4MDQ1MDUsImlhdCI6MTcxMTcwMDUwNSwianRpIjoiNTQ4ZDA5ZWUtMGM3OS00MjU4LTg4ZGUtZjFmMTYxOTQ5NGJlIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo5MDkwL3JlYWxtcy9zcHJpbmdib290LW1pY3Jvc2VydmljZS1yZWFsbSIsInN1YiI6IjEwMDNjNWU1LTgzODQtNGZkYi05NjFhLWJmNWMwYWY5MTAyYSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImdhdGV3YXktY2xpZW50IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIvKiJdLCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxOTIuMTY4LjY0LjEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtZ2F0ZXdheS1jbGllbnQiLCJjbGllbnRBZGRyZXNzIjoiMTkyLjE2OC42NC4xIiwiY2xpZW50X2lkIjoiZ2F0ZXdheS1jbGllbnQifQ.RbWpqNWxlbAC5VN3x7B-iemf0mk_sODnAKEbEV3kOEVwmTwTRreIfGlAMp9pwWoYkqB3nEfz2pPrv3Gy1KaaXMqVvX84Vu0CLbqRcQjyr5_cKq_fGN7E_VrmExCga_EDtHbQdksH3wFdpY0nvYhpIoGpxk4xIMUvVlrwGlyrI4nTeYh7D8cJ0_VRgdW0QvXtmClizRbG7zt61buktRtZ8ity8P0roWuTbp4N_3pI4EiJUfvfUA8zFnmg-E3OZkIE5Hic-BDEr8glSpwtzZ2UCafc-deYKbWZrPY-gSQPyLa8BQJJ9oDvTxBTJd0a_2LgeNF7kujJAl-Qneyfr6oChw"

with open('workflow.yml', 'r') as file:
    workflow = file.read()
remote_artifact_workflow = provider.create_artifact(data={"value": workflow, "title": "workflow.yml"})
data_output ={
    "accessUrl": backend_url + "/output",
    "title": "output.jsonl",
    "apiKey": {"key":"Authorization", "value": apiKey}
}
remote_artifact_output = provider.create_artifact(data=data_output)
remote_artifact_trigger = provider.create_artifact(data={
    "accessUrl": backend_url,
    "title": "service_base_access_url",
    "apiKey": {"key":"Authorization", "value": apiKey}
})
contract_data = data={
    "start": "2023-04-06T13:33:44.995+02:00",
    "end": "2026-12-06T13:33:44.995+02:00",
}
contract = provider.create_contract(data=contract_data)

n_time_usage_rule = provider.create_rule(
    data={
        "value": """{
        "@context" : {
            "ids" : "https://w3id.org/idsa/core/",
            "idsc" : "https://w3id.org/idsa/code/"
        },
      "@type": "ids:Permission",
      "@id": "https://w3id.org/idsa/autogen/permission/154df1cf-557b-4f44-b839-4b68056606a2",
      "ids:description": [
        {
          "@value": "n-times-usage",
          "@type": "http://www.w3.org/2001/XMLSchema#string"
        }
      ],
      "ids:title": [
        {
          "@value": "Example Usage Policy",
          "@type": "http://www.w3.org/2001/XMLSchema#string"
        }
      ],
      "ids:action": [
        {
          "@id": "idsc:USE"
        }
      ],
      "ids:constraint": [
        {
          "@type": "ids:Constraint",
          "@id": "https://w3id.org/idsa/autogen/constraint/4ae656d1-2a73-44e3-a168-b1cbe49d4622",
          "ids:rightOperand": {
            "@value": "1000",
            "@type": "http://www.w3.org/2001/XMLSchema#double"
          },
          "ids:leftOperand": {
            "@id": "idsc:COUNT"
          },
          "ids:operator": {
            "@id": "idsc:LTEQ"
          }
        }
      ]
    }"""
    }
)

## Link Resources
provider.add_resource_to_catalog(catalog, offers)
provider.add_representation_to_resource(offers, representation_trigger)
provider.add_representation_to_resource(offers, representation_workflow)
provider.add_representation_to_resource(offers, representation_output)
provider.add_artifact_to_representation(representation_trigger, remote_artifact_trigger)
provider.add_artifact_to_representation(representation_workflow, remote_artifact_workflow)
provider.add_artifact_to_representation(representation_output, remote_artifact_output)
provider.add_contract_to_resource(offers, contract)
provider.add_rule_to_contract(contract, n_time_usage_rule)

print("Created provider resources")

provider.push_to_broker(broker_url,offers.replace("localhost","service-provider"))

# # Consumer
# consumer = IdsApi(consumer_url)
#
# ##
# catalogResponse = consumer.descriptionRequest(provider_url + "/api/ids/data", catalog)
# obj = catalogResponse["ids:offeredResource"][0]
# resourceId1 = obj["@id"]
# contract = obj["ids:contractOffer"][0]
# contractId = contract["@id"]
# representation = obj["ids:representation"][0]
# artifact = representation["ids:instance"][0]
# artifactId1 = artifact["@id"]
#
# ##
# contract1Response = consumer.descriptionRequest(
#     provider_url + "/api/ids/data", contractId
# )
#
#
#
# ##
# count = contract1Response["ids:permission"][0]
# count["ids:target"] = artifactId1
#
# ##
# body = [count]
# resources = [resourceId1]
# artifacts = [artifactId1]
# response = consumer.contractRequest(
#     provider_url + "/api/ids/data", resources, artifacts, True, body
# )
# pprint.pprint(response)
