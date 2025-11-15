import React, { useState } from "react";
import {
	Box,
	Container,
	Paper,
	Typography,
	Button,
	Alert,
	CircularProgress,
	Card,
	CardContent,
	Chip,
	Stack,
	ThemeProvider,
	createTheme,
	CssBaseline,
} from "@mui/material";
import { CloudUpload, CheckCircle, Description } from "@mui/icons-material";

const theme = createTheme({
	palette: {
		mode: "light",
		primary: {
			main: "#1976d2",
		},
		secondary: {
			main: "#dc004e",
		},
		background: {
			default: "#f5f5f5",
		},
	},
	typography: {
		fontFamily: '"Segoe UI", "Roboto", "Helvetica", "Arial", sans-serif',
	},
});

function App() {
	const [selectedFile, setSelectedFile] = useState<File | null>(null);
	const [uploading, setUploading] = useState(false);
	const [response, setResponse] = useState<any>(null);
	const [error, setError] = useState<string | null>(null);

	const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		if (event.target.files && event.target.files[0]) {
			setSelectedFile(event.target.files[0]);
			setResponse(null);
			setError(null);
		}
	};

	const handleUpload = async () => {
		if (!selectedFile) {
			setError("Please select a file first");
			return;
		}

		setUploading(true);
		setError(null);
		setResponse(null);

		try {
			const formData = new FormData();
			formData.append("file", selectedFile);

			const res = await fetch("http://localhost:8000/upload/", {
				method: "POST",
				body: formData,
			});

			if (!res.ok) {
				throw new Error(`Upload failed: ${res.statusText}`);
			}

			const data = await res.json();
			setResponse(data);
		} catch (err) {
			setError(err instanceof Error ? err.message : "Upload failed");
		} finally {
			setUploading(false);
		}
	};

	return (
		<ThemeProvider theme={theme}>
			<CssBaseline />
			<Box
				sx={{
					minHeight: "100vh",
					background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
					display: "flex",
					alignItems: "center",
					justifyContent: "center",
					padding: 3,
				}}
			>
				<Container maxWidth="md">
					<Paper
						elevation={8}
						sx={{
							padding: 3,
							borderRadius: 3,
							background: "rgba(255, 255, 255, 0.95)",
							backdropFilter: "blur(10px)",
						}}
					>
						<Stack spacing={3} alignItems="center">
							<Description sx={{ fontSize: 40, color: "primary.main" }} />
							<Typography variant="h3" component="h1" fontWeight="bold" color="primary">
								Document Upload
							</Typography>
							<Typography variant="body1" color="text.secondary" textAlign="center">
								Upload your documents securely and receive instant processing results
							</Typography>

							<Box sx={{ width: "100%", mt: 2 }}>
								<input
									accept="*/*"
									style={{ display: "none" }}
									id="file-upload"
									type="file"
									onChange={handleFileChange}
									disabled={uploading}
								/>
								<label htmlFor="file-upload">
									<Button
										variant="outlined"
										component="span"
										fullWidth
										startIcon={<CloudUpload />}
										disabled={uploading}
										sx={{ py: 2, mb: 2 }}
									>
										{selectedFile ? selectedFile.name : "Choose File"}
									</Button>
								</label>

								{selectedFile && (
									<Card variant="outlined" sx={{ mb: 2 }}>
										<CardContent>
											<Stack direction="row" spacing={2} alignItems="center">
												<Description color="primary" />
												<Box sx={{ flexGrow: 1 }}>
													<Typography variant="body2" fontWeight="medium">
														{selectedFile.name}
													</Typography>
													<Typography variant="caption" color="text.secondary">
														{(selectedFile.size / 1024).toFixed(2)} KB
													</Typography>
												</Box>
												<Chip label="Ready" color="success" size="small" />
											</Stack>
										</CardContent>
									</Card>
								)}

								<Button
									variant="contained"
									onClick={handleUpload}
									disabled={!selectedFile || uploading}
									fullWidth
									size="large"
									startIcon={uploading ? <CircularProgress size={20} color="inherit" /> : <CheckCircle />}
									sx={{ py: 1.5 }}
								>
									{uploading ? "Uploading..." : "Upload Document"}
								</Button>
							</Box>

							{error && (
								<Alert severity="error" sx={{ width: "100%", mt: 2 }}>
									{error}
								</Alert>
							)}

							{response && (
								<Card
									sx={{
										width: "100%",
										mt: 3,
										background: "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)",
									}}
								>
									<CardContent>
										<Stack spacing={2}>
											<Typography variant="h6" color="primary" fontWeight="bold">
												Upload Successful
											</Typography>
											<Box
												component="pre"
												sx={{
													backgroundColor: "#263238",
													color: "#aed581",
													padding: 2,
													borderRadius: 2,
													overflow: "auto",
													fontSize: "0.875rem",
													fontFamily: '"Consolas", "Monaco", "Courier New", monospace',
												}}
											>
												{JSON.stringify(response, null, 2)}
											</Box>
										</Stack>
									</CardContent>
								</Card>
							)}
						</Stack>
					</Paper>
				</Container>
			</Box>
		</ThemeProvider>
	);
}

export default App;
