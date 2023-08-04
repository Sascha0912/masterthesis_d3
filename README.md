# StudyU Extension
## as a part of the masterthesis

This is the implementation of the StudyU extension.
This is a work in progress version and should not be used in production.

## Data

The required data format is JSON.
The data needs to be prepared in the following way:
```json
{
  "metadata": [
    "name": <String>,
    "time unit": <String>,
    "info": <String>,
    "treatment1_name": <String>,
    "treatment2_name": <String>
    
  ],
  "data": [
    {
      "id": <number, unique>,
      "value": <float>,
      "avg": <float>,
      "treatment": <String>
    },
    {
      "id": <number, unique>,
      "value": <float>,
      "avg": <float>,
      "treatment": <String>
    },
    ...
  ]
}
```
For each data series a separate JSON file must be created.