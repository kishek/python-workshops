NUM_REQUESTS="$1"
echo "[generate-logs]: executing $1 requests..."
for i in {0..NUM_REQUESTS}; do
    curl -X GET http://localhost:5000/deepcheck
done