DROP TABLE IF EXISTS leads;
DROP TABLE IF EXISTS clicks;
DROP TABLE IF EXISTS offers;


CREATE TABLE IF NOT EXISTS leads (
       lead_uuid VARCHAR(255),
       requested float(8),
       loan_purpose VARCHAR(255),
       credit VARCHAR(255),
       annual_income float(8)
);

CREATE TABLE IF NOT EXISTS clicks (
       offer_id INT,
       clicked_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS offers (
       lead_uuid VARCHAR(255),
       offer_id INT,
       apr float(8),
       lender_id INT
);