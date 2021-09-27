-- Role: genuser
-- DROP ROLE genuser;

CREATE ROLE genuser WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION
  ENCRYPTED PASSWORD 'gen_user_password';

GRANT generic_role TO genuser;

COMMENT ON ROLE genuser IS 'Generic User';