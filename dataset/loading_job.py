import pyTigerGraph as tg

# connection parameters
# hostname is the TigerGraph solution URL
host_name = "https://my-medic-ai.i.tgcloud.io"
graph_name = "drugs"
user_name = "tigergraph"
password = "tigergraph"


# establish connection to the TigerGraph solution
conn = tg.TigerGraphConnection(host=host_name, username=user_name, password=password)

# print the current schema to verify that i'm connected
print(conn.gsql('LS'))