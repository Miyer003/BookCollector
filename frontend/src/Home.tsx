import React from 'react';
import Paper from '@mui/material/Paper';
import Card from '@mui/material/Card';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';

// ECharts马卡龙配色
const macaronsColors = [
      '#2ec7c9', '#b6a2de', '#5ab1ef', '#ffb980',
      '#d87a80', '#8d98b3', '#e5cf6e', '#97b552',
      '#95706d', '#dc69aa', '#07a2a4', '#9a7fd1',
      '#588dd5', '#f5994e', '#c05050', '#59678c',
      '#c9ab00', '#7eb00a', '#6f5553', '#c14089'
];
// 随机取色
const getRandomColor = () => macaronsColors[Math.floor(Math.random() * macaronsColors.length)];

export default function Home() {
  return (
    <div>
        <Box>
            <Paper elevation={3} style={{ padding: '20px', marginBottom: '20px', background: getRandomColor() }}>
                <h1>Welcome! MY</h1>
                <h6>刷新有惊喜～</h6>
                <p>Your personal book collection management system.</p>
            </Paper>
            <Card style={{ padding: '20px', marginBottom: '20px', background: getRandomColor() }}>
                <h2>Get Started</h2>
                <Button variant="contained" color="primary" href="/add-book">
                    Add a New Book
                </Button>
            </Card>
            <Card style={{ padding: '20px', background: getRandomColor() }}>
                <h2>Features</h2>
                <ul>
                    <li>Manage your book collection</li>
                    <li>Track reading progress</li>
                    <li>Share your collection with friends</li>
                </ul>
            </Card>
        </Box>
        <Box style={{ marginTop: '20px', textAlign: 'center', background: getRandomColor() }}>
            <Button variant="outlined" color="secondary" href="/about">
                Learn More About Us
            </Button>
        </Box>
    </div>
  );
}