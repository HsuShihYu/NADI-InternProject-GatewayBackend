data = {
  "System": "TEST",
  "TimeStamp": 1234567890,
  "TimeZone": "Asia/Taipei",
  "Data": [
    {
      "ObjectId": "BL_202_Run_000001",
      "Value": "5560",
      "TimeStamp":1583816575
    },
    {
      "ObjectId": "BL_202_Idle_000002",
      "Value": "5000",
      "TimeStamp":1583816580
    },
    {
      "ObjectId": "BL_202_Status_000007",
      "Value": "14789",
      "TimeStamp":1583816587
    }
    ]
}
print(len(data["Data"]))
for row in data["Data"]:
    _object_id = row['ObjectId']
    print(_object_id)