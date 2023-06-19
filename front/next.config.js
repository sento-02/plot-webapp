/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    SERVER_URL: process.env.SERVER_URL,
  },
  async rewrites() {
    return [
      {
        source: '/init',
        destination: `${process.env.SERVER_URL}/init`,
      },
      {
        source: '/graph',
        destination: `${process.env.SERVER_URL}/test_graph`,
      },
      {
        source: '/:hash*',
        destination: `${process.env.SERVER_URL}/:hash*`,
      },
    ]
  },
}

module.exports = nextConfig
