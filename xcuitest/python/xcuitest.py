import requests
import json
import base64

username = ''
apiKey = ''

encodeAuth = 'Basic ' + (base64.b64encode((username + ':' + apiKey).encode('utf-8'))).decode('utf-8')

url = 'https://api.kobiton.com/hub/session'

configuration = {
  'configuration': {
    'sessionName': 'Automation test session',
    'sessionDescription': 'This is an example for XCUITest testing',
    'deviceName': '',
    'platformVersion':  '',
    'deviceGroup': 'KOBITON',
    'app': 'https://kobiton-devvn.s3-ap-southeast-1.amazonaws.com/apps-test/XCUITestSample.ipa',
    'testRunner': 'https://kobiton-devvn.s3-ap-southeast-1.amazonaws.com/apps-test/XCUITestSampleUITestRunner.ipa',
    'testFramework': 'XCUITEST',
    'sessionTimeout': 30,

    # The user can specifically test running via testPlan or tests
    # If the testPlan and tests are set, the test framework will auto-select the testPlan first
    'tests': [],
    'testPlan': 'https://kobiton-devvn.s3-ap-southeast-1.amazonaws.com/apps-test/sample.xctestplan'
  }
}

configuration_str = json.dumps(configuration)
headers = {
  'Content-Type': 'application/json',
  'Authorization': encodeAuth,
  'Accept':'application/json'
}

response = requests.request('POST', url, headers=headers, data = configuration_str)
print(response.text.encode('utf8'))
