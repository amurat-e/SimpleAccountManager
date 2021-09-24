-- FUNCTION: public.delete_account_table(integer)

-- DROP FUNCTION public.delete_account_table(integer);

CREATE OR REPLACE FUNCTION public.delete_account_table(
	actid integer)
    RETURNS text
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE 
pswid integer;
BEGIN
			SELECT act_id INTO STRICT pswid FROM public.accounts WHERE act_id = actid;
			DELETE FROM public.accounts WHERE act_id = actid;
			RETURN 'Ok...';
		EXCEPTION
			WHEN NO_DATA_FOUND THEN
				RAISE INFO 'Error Name:%',SQLERRM;
        		RAISE INFO 'Error State:%', SQLSTATE;
        		RETURN 'Account Id:'|| actid::text ||' Record Not Found. ['||SQLSTATE||':'||SQLERRM||']';
			WHEN OTHERS THEN
				RAISE INFO 'Error Name:%',SQLERRM;
        		RAISE INFO 'Error State:%', SQLSTATE;
        		RETURN SQLSTATE||':'||SQLERRM;
	
END;
$BODY$;

ALTER FUNCTION public.delete_account_table(integer)
    OWNER TO postgres;

GRANT EXECUTE ON FUNCTION public.delete_account_table(integer) TO PUBLIC;

GRANT EXECUTE ON FUNCTION public.delete_account_table(integer) TO generic_role WITH GRANT OPTION;

GRANT EXECUTE ON FUNCTION public.delete_account_table(integer) TO postgres;

