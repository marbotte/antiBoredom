CREATE TABLE antiboredom_log
(
    id SERIAL PRIMARY KEY,
    date_time TIMESTAMP DEFAULT NOW(),
    type_act VARCHAR(50),
    unrecognized BOOLEAN,
    activity TEXT,
    key_act BIGINT,
    error BOOLEAN,
    joke TEXT,
    id_joke BIGINT,
    word VARCHAR(250)
);
