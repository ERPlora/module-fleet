# Fleet Management Module

Vehicle fleet tracking, fuel consumption, and maintenance management.

## Features

- Register and manage vehicles with make, model, year, plate number, and fuel type
- Track vehicle status: available, in use, in maintenance, retired
- Assign vehicles to staff members
- Record fuel consumption logs with liters, cost, odometer, and station details
- Log trips with origin, destination, distance, driver, and purpose
- Track vehicle maintenance records (preventive, corrective, inspection/ITV) with cost and workshop details
- Schedule next maintenance by date or odometer reading
- Monitor odometer readings across fuel logs and maintenance
- Dashboard with fleet overview and key metrics

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Fleet Management > Settings**

## Usage

Access via: **Menu > Fleet Management**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/fleet/dashboard/` | Overview of fleet status, fuel costs, and maintenance schedule |
| Vehicles | `/m/fleet/vehicles/` | List, create, and manage vehicles and their logs |
| Settings | `/m/fleet/settings/` | Configure fleet management module settings |

## Models

| Model | Description |
|-------|-------------|
| `Vehicle` | Vehicle record with make, model, year, plate number, fuel type, odometer, status, and assignment |
| `FuelLog` | Fuel consumption record with date, liters, cost, odometer reading, and station |
| `TripLog` | Trip record with origin, destination, distance, driver, and purpose |
| `VehicleMaintenanceLog` | Maintenance record with type (preventive/corrective/inspection), cost, workshop, and next maintenance scheduling |

## Permissions

| Permission | Description |
|------------|-------------|
| `fleet.view_vehicle` | View vehicles and their logs |
| `fleet.add_vehicle` | Create new vehicles |
| `fleet.change_vehicle` | Edit vehicles and their logs |
| `fleet.delete_vehicle` | Delete vehicles |
| `fleet.manage_settings` | Manage fleet management module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
