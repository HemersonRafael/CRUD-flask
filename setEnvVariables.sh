export FLASK_ENV=development
export DATABASE_URL=postgres://apiflask:123456@localhost:5432/blog_api_db
export JWT_SECRET_KEY=hhgaghhgsdhdhdd
export PORT=5000
echo "FLASK_ENV=" $FLASK_ENV
echo "DATABASE_URL="$DATABASE_URL
echo "JWT_SECRET_KEY="$JWT_SECRET_KEY
echo "PORT="$PORT
echo "Success set environment variables!"