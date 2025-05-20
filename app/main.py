from fastapi import FastAPI

app = FastAPI(title="Readcommend API")

@app.get("/", tags=["Health"])
async def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok", "message": "FastAPI backend is healthy!"}

# You can also import and test the supabase client here if you want
# from app.db.supabase_client import supabase_client
# @app.get("/test-supabase", tags=["Health"])
# async def test_supabase():
#     try:
#         # Example: try to list tables (requires service_role)
#         # This is just a placeholder, actual queries will be more specific
#         response = supabase_client.table('profiles').select('id').limit(1).execute()
#         return {"supabase_connection": "successful", "data": response.data}
#     except Exception as e:
#         return {"supabase_connection": "failed", "error": str(e)}