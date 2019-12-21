# Taking the first argument from the running of the script
NUM_REQUESTS="$1"
# Logging a string to the terminal/output stream
echo "[generate-logs]: executing $NUM_REQUESTS requests..."
# A loop which runs the command inside the loop $NUM_REQUESTS times.
for i in $( eval echo {0..$NUM_REQUESTS} ); do
    curl -X GET http://localhost:5000/deepcheck
done