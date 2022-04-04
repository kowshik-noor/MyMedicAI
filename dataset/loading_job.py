import pyTigerGraph as tg

# connection parameters
# hostname is the TigerGraph solution URL
host_name = "https://my-medic-ai.i.tgcloud.io"
graph_name = "drugs"
user_name = "tigergraph"
password = "tigergraph"


# establish connection to the TigerGraph solution
conn = tg.TigerGraphConnection(host=host_name, username=user_name, password=password)

# GRAPH CONNECTION
# creating the secret and token that's needed to authenticate our graph

# set the name of graph to connect to
conn.graphname = graph_name

# create a secret
secret = conn.createSecret()
# use the secret to get a token
auth_token = conn.getToken(secret)[0]

# connect to the graph with the token
conn = tg.TigerGraphConnection(host=host_name, 
    username=user_name, 
    password=password, 
    graphname=graph_name,
    apiToken=auth_token)

# listing vertex count requires graph authentication
# print(conn.getVertexCount("*"))

conn.gsql('''
USE GRAPH drugs
CREATE LOADING JOB load_products FOR GRAPH drugs {
    DEFINE FILENAME MyDataSource;
    LOAD MyDataSource TO VERTEX Product VALUES(gsql_concat($1,",",$5), $5, $3, $4, $7) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO VERTEX Form VALUES($2) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO VERTEX ActiveIngredient VALUES($6) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_form VALUES(gsql_concat($1,",",$5), $2) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_active_ingredient VALUES(gsql_concat($1,",",$5), $6) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_application VALUES(gsql_concat($1,",",$5), $0) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
}
CREATE LOADING JOB load_application_data FOR GRAPH drugs {
    DEFINE FILENAME MyDataSource;
    LOAD MyDataSource TO VERTEX Application VALUES($0, $2) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO VERTEX Sponsor VALUES($0, $3) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO VERTEX ApplicationType VALUES($0, $1) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_sponsor VALUES($0, $3) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_type VALUES($0, $1) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
}
CREATE LOADING JOB load_te FOR GRAPH drugs {
    DEFINE FILENAME MyDataSource;
    LOAD MyDataSource TO VERTEX TE VALUES($3) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
    LOAD MyDataSource TO EDGE has_te VALUES($0, $3) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
}
CREATE LOADING JOB load_marketing_lookup FOR GRAPH drugs {
    DEFINE FILENAME MyDataSource;
    LOAD MyDataSource TO VERTEX MarketingStatus VALUES($0, $1) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
}
CREATE LOADING JOB load_marketing FOR GRAPH drugs {
    DEFINE FILENAME MyDataSource;
    LOAD MyDataSource TO EDGE has_marketing_status VALUES($1, $0) USING SEPARATOR="\t", HEADER="false", EOL="\n" QUOTE="none";
}

''')