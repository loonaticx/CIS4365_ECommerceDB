BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Account" (
	id INTEGER NOT NULL, 
	uuid VARCHAR(32), 
	username VARCHAR(64), 
	email VARCHAR(128), 
	pass_hash VARCHAR(128), 
	registered_on VARCHAR(128), 
	last_login VARCHAR(128), 
	PRIMARY KEY (id), 
	UNIQUE (uuid)
);
CREATE TABLE IF NOT EXISTS "Customer" (
	id INTEGER NOT NULL, 
	uuid VARCHAR(32), 
	account_id INTEGER, 
	personal_info_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (uuid), 
	FOREIGN KEY(account_id) REFERENCES "Account" (id), 
	FOREIGN KEY(personal_info_id) REFERENCES "PersonalInfo" (id)
);
CREATE TABLE IF NOT EXISTS "CustomerShoppingCart" (
	id INTEGER NOT NULL, 
	uuid VARCHAR(32), 
	PRIMARY KEY (id), 
	UNIQUE (uuid)
);
CREATE TABLE IF NOT EXISTS "PersonalInfo" (
	id INTEGER NOT NULL, 
	first_name VARCHAR(64), 
	last_name VARCHAR(64), 
	uuid VARCHAR(32), 
	PRIMARY KEY (id), 
	UNIQUE (uuid)
);
CREATE TABLE IF NOT EXISTS "Product" (
	id INTEGER NOT NULL, 
	name VARCHAR(64), 
	uuid VARCHAR(32), 
	PRIMARY KEY (id), 
	UNIQUE (uuid)
);
CREATE TABLE IF NOT EXISTS "PurchaseRecord" (
	id INTEGER NOT NULL, 
	uuid VARCHAR(32), 
	product_id INTEGER, 
	name VARCHAR(512), 
	PRIMARY KEY (id), 
	UNIQUE (uuid), 
	FOREIGN KEY(product_id) REFERENCES "Product" (id)
);
INSERT INTO "Customer" VALUES (1,'QIHtZenqwYLLcHrHpu0s0RizeMo_IHo9_a2_66hmex4',NULL,NULL);
COMMIT;
