select distinct json_array_elements((event_value::JSON->>'product_payments')::JSON)::JSON->>'product_name' AS product_name
FROM public.outbox
where (event_value::JSON->>'product_payments')::JSON is not null;