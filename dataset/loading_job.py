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
print(conn.getVertexCount("*"))