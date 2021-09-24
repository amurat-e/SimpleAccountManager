-- Role: generic_role
-- DROP ROLE generic_role;

CREATE ROLE generic_role WITH
  NOLOGIN
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION;

COMMENT ON ROLE generic_role IS 'Standard role';