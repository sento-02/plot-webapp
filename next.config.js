/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig

module.exports = {
    async rewrites() {
      return [
        {
          source: '/test/file_list',
          destination: 'http://10.100.53.90:80/test_file_list',//chenge here
        },
        {
            source: '/test/graph',
            destination: 'http://10.100.53.90:80/test_graph',//change here
            // destination: 'http://10.100.53.90:80/test_graph',
        },
        {
          source: '/src/[hash]',
          destination: 'http://10.100.53.90:80/[hash]',//change here
        },
      ];
    },
  };