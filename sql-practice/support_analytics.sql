-- SQL Practice: Support Incident Analysis
-- Author: Olena Belichenko

-- 1. Table Structure (Schema)
CREATE TABLE Incidents (
    id INTEGER PRIMARY KEY,
    service_name TEXT,
    priority TEXT,
    status TEXT,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Query: Find all critical incidents that are not yet closed
SELECT service_name, priority, status 
FROM Incidents 
WHERE priority = 'Critical' AND status != 'Closed';

-- 3. Query: Count incidents per service (Aggregation)
SELECT service_name, COUNT(*) as incident_count
FROM Incidents
GROUP BY service_name
ORDER BY incident_count DESC;

-- 4. Advanced Query: Join Users and their Tickets
-- Retrieve user email and incident status for High-priority issues
SELECT Users.email, Incidents.service_name, Incidents.status
FROM Users
JOIN Incidents ON Users.id = Incidents.user_id
WHERE Incidents.priority = 'High';
