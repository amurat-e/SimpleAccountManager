-- SEQUENCE: public.account_act_id_seq

-- DROP SEQUENCE public.account_act_id_seq;

CREATE SEQUENCE public.account_act_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.account_act_id_seq
    OWNER TO postgres;

GRANT ALL ON SEQUENCE public.account_act_id_seq TO generic_role WITH GRANT OPTION;

GRANT ALL ON SEQUENCE public.account_act_id_seq TO postgres;