const url = require("url");
const MongoClient = require("mongodb").MongoClient;

// Create cached connection variable
let cachedDb = null;

async function connectToDatabase(uri) {
  // If the database connection is cached,
  // use it instead of creating a new connection
  if (cachedDb) {
    return cachedDb;
  }

  // If no connection is cached, create a new one
  const client = await MongoClient.connect(uri, {
    // useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  const db = await client.db(url.parse(uri).pathname.substr(1));
  cachedDb = db;

  return db;
}

module.exports = async (req, res) => {
  const db = await connectToDatabase(process.env.MONGODB_URI);

  const collection = await db.collection("humidity");
  const readings = await collection.find({}).sort({ _id: -1 }).toArray();

  res.status(200).json({ readings });
};
