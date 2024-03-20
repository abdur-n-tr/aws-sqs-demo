## AWS SQS Demo Instructions

- Create an SQS standard queue


- For producer lambda, assign SQS permission to IAM. This will produce data in SQS.
- For consumer lambda, assign SQS and s3 permission to IAM. This will consume data from SQS via EventBridge pipe and process it
and save it in s3 bucket.

- Create s3 bucket and attach bucket policy for AWS Lambda

- Create Event Bridge pipe with SQS as Source and Lambda as Target. Put the below transformer payload in Pipe target.

```bash
{
  "booking_id": <$.body.bookingId>,
  "user_id": <$.body.userId>,
  "property_id": <$.body.propertyId>,
  "location": <$.body.location>,
  "start_date": <$.body.startDate>,
  "end_date": <$.body.endDate>,
  "price": <$.body.price>
}
```