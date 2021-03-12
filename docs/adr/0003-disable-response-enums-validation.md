# 3. Disable response enums validation

Date: 2021-03-12

## Status

Accepted

## Context

Several resources of Kentik API v5 have fields with a defined set of values, which are represented as enums in the code. Possible enum values are specified in the API documentation ((e.g. [device types][1] or [device BGP settings][2])).

When Kentik API returns enum values other than defined in the code, a _ValueError_ error is returned by the library. The documentation is not up to date with all possible enum values, so such case is happening frequently.

[1]: https://kb.kentik.com/v3/Cb01.htm#Cb01-Supported_Device_Types
[2]: https://kb.kentik.com/v3/Cb01.htm#Cb01-Device_BGP_Settings

## Decision

The code will be modified not to return the error when unknown enum is found in response.

## Consequences

Using of the library will be easier, because a whole category of errors will be eliminated.
