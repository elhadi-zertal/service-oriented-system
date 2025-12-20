CREATE TABLE IF NOT EXISTS system_logs(
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(50) NOT NULL,
    log_message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO system_logs (service_name, log_message) VALUES
('nginx', 'reverse proxy started'),
('backend', 'API service initialized'),
('postgres', 'database connection established');


