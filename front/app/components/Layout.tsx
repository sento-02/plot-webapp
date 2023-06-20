import React from 'react';
import { Container, Box, AppBar, Toolbar, Typography } from '@mui/material';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">My App</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="md">
        <Box my={4}>{children}</Box>
      </Container>
      <Box mt={8} py={3} textAlign="center" style={{ backgroundColor: "#f7f7f7" }}>
        <Typography variant="body2" color="textSecondary">
          © 2023 My App
        </Typography>
      </Box>
    </Box>
  );
};

export default Layout;
