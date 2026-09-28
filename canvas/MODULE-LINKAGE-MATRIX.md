# ECCS Hub Module Linkage Matrix

Hub app: `canvas/ECCS - Registration POC.msapp`
Hub screen: `scrModuleHub`

| Module key | Module name | Launch mode | Hub target | Landing screen | Required params |
| --- | --- | --- | --- | --- | --- |
| registration_core | Registration Core | Screen (same app) | `scrRegistrationCore` | `scrRegistrationCore` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| cnet | CNET | App deep link | `ECCS_APPID_CNET` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| emergency_department | Emergency Department | App deep link | `ECCS_APPID_EMERGENCY_DEPARTMENT` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| mis_provider | MIS Provider | App deep link | `ECCS_APPID_MIS_PROVIDER` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_consults | Non-Med Consults | App deep link | `ECCS_APPID_NON_MED_CONSULTS` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_diet | Non-Med Diet | App deep link | `ECCS_APPID_NON_MED_DIET` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_ekg | Non-Med EKG | App deep link | `ECCS_APPID_NON_MED_EKG` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_level_of_care | Non-Med Level of Care | App deep link | `ECCS_APPID_NON_MED_LEVEL_OF_CARE` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_nursing | Non-Med Nursing | App deep link | `ECCS_APPID_NON_MED_NURSING` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_oe | Non-Med OE | App deep link | `ECCS_APPID_NON_MED_OE` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_rad | Non-Med RAD | App deep link | `ECCS_APPID_NON_MED_RAD` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| non_med_rt_pt_ot | Non-Med RT/PT/OT | App deep link | `ECCS_APPID_NON_MED_RT_PT_OT` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |
| registration_ptac | Registration PTAC | App deep link | `ECCS_APPID_REGISTRATION_PTAC` | `scrModuleMain` | moduleKey, facility, recordKey, targetEnvironment, userPrincipalName, userDisplayName, sourceScreen, searchText |

## Return path standard

- In-app modules: `Back()` to `scrModuleHub` with `varNavContext` retained.
- External modules: return with a launch URL to the hub app and include `moduleKey`, `facility`, `targetEnvironment`, `userPrincipalName`, `userDisplayName`, `sourceScreen`, `searchText`, and optional `returnRecordKey` (mapped into `recordKey`), `returnToast`, and `launchUtc` query parameters.
- Hub startup should hydrate state from params and reapply facility filter, selected record, and search text.

## Validation execution log template

Run one pass for each module:

1. Select a facility and search value on `scrModuleHub`.
2. Launch module target from registry-driven control.
3. Confirm landing screen and context hydration.
4. Modify one record and save against module Dataverse table.
5. Return to hub and confirm facility/search/record state are preserved.
6. Record result as PASS/FAIL with notes.
