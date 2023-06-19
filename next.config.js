/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig

module.exports = {
    async rewrites() {
      return [
        {
          source: '/test_file_list',
          destination: 'http://192.168.179.3:80/test_file_list',//chenge here
        },
        {
            source: '/test_graph',
            destination: 'http://192.168.179.3:80/test_graph',//change here
            // destination: 'http://10.100.53.90:80/test_graph',
        },
        {
          source: '/:hash*',
          destination: 'http://192.168.179.3:80/:hash*',//change here
        },
      ];
    },
  };