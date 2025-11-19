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
	TextField,
	Divider,
} from "@mui/material";
import { CloudUpload, CheckCircle, Description, TextFields, ExpandLess, ExpandMore } from "@mui/icons-material";

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
	const [text, setText] = useState<string>("");
	const [uploading, setUploading] = useState(false);
	const [response, setResponse] = useState<any>(null);
	const [extraction, setExtraction] = useState<any>(null);
	const [steps, setSteps] = useState<string[] | null>(null);
	const [error, setError] = useState<string | null>(null);

	const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		if (event.target.files && event.target.files[0]) {
			setSelectedFile(event.target.files[0]);
			setResponse(null);
			setError(null);
		}
	};

	const handleTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
		setText(event.target.value);
		setResponse(null);
		setError(null);
	};

	const [extractionExpanded, setExtractionExpanded] = useState(false);
	const [stepsExpanded, setStepsExpanded] = useState(false);

	const handleFileUpload = async () => {
		if (!selectedFile) {
			setError("Please select a file first");
			return;
		}
        setExtractionExpanded(false);
        setStepsExpanded(false);

		setUploading(true);
		setError(null);
		setResponse(null);

		try {
			const formData = new FormData();
			formData.append("file", selectedFile);

			const res = await fetch("http://localhost:8000/audit/file", {
				method: "POST",
				body: formData,
			});

			if (!res.ok) {
				throw new Error(`Upload failed: ${res.statusText}`);
			}

			const data = await res.json();
			setResponse(data.result);
			setExtraction(data.extraction);
			setSteps(data.steps);
		} catch (err) {
			setError(err instanceof Error ? err.message : "Upload failed");
		} finally {
			setUploading(false);
		}
	};

	const handleTextSubmit = async () => {
		if (!text.trim()) {
			setError("Please enter some text first");
			return;
		}

        setExtractionExpanded(false);
        setStepsExpanded(false);

		setUploading(true);
		setError(null);
		setResponse(null);

		try {
			const res = await fetch("http://localhost:8000/audit/text", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({ text }),
			});

			if (!res.ok) {
				throw new Error(`Submission failed: ${res.statusText}`);
			}

			const data = await res.json();
			setResponse(data.result);
			setExtraction(data.extraction);
			setSteps(data.steps);
		} catch (err) {
			setError(err instanceof Error ? err.message : "Submission failed");
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
				<Container maxWidth="lg">
					<Paper
						elevation={8}
						sx={{
							padding: 4,
							borderRadius: 3,
							background: "rgba(255, 255, 255, 0.95)",
							backdropFilter: "blur(10px)",
						}}
					>
						<Stack spacing={3} alignItems="center">
							<Description sx={{ fontSize: 60, color: "primary.main" }} />
							<Typography variant="h3" component="h1" fontWeight="bold" color="primary">
								Document Auditor
							</Typography>
							<Typography variant="body1" color="text.secondary" textAlign="center">
								Upload a document or paste text for instant audit analysis
							</Typography>

							<Box
								sx={{
									display: "flex",
									flexDirection: { xs: "column", md: "row" },
									gap: 3,
									width: "100%",
									mt: 2,
								}}
							>
								{/* Left Pane - File Upload */}
								<Box sx={{ flex: 1, minWidth: 0 }}>
									<Paper variant="outlined" sx={{ p: 3, height: "100%", minHeight: "100px" }}>
										<Stack spacing={2}>
											<Stack direction="row" spacing={1} alignItems="center">
												<CloudUpload color="primary" />
												<Typography variant="h6" fontWeight="bold">
													Upload Document
												</Typography>
											</Stack>
											<Divider />

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
													sx={{ py: 2 }}
												>
													{selectedFile ? selectedFile.name : "Choose File"}
												</Button>
											</label>

											{selectedFile && (
												<Card variant="outlined">
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
												onClick={handleFileUpload}
												disabled={!selectedFile || uploading}
												fullWidth
												size="large"
												startIcon={
													uploading ? (
														<CircularProgress size={20} color="inherit" />
													) : (
														<CheckCircle />
													)
												}
												sx={{ py: 1.5, mt: "auto" }}
											>
												{uploading ? "Processing..." : "Upload & Audit"}
											</Button>
										</Stack>
									</Paper>
								</Box>

								{/* Right Pane - Text Input */}
								<Box sx={{ flex: 1, minWidth: 0 }}>
									<Paper variant="outlined" sx={{ p: 3, height: "100%", minHeight: "100px" }}>
										<Stack spacing={2} sx={{ height: "100%" }}>
											<Stack direction="row" spacing={1} alignItems="center">
												<TextFields color="primary" />
												<Typography variant="h6" fontWeight="bold">
													Paste or Type Text
												</Typography>
											</Stack>
											<Divider />

											<TextField
												multiline
												rows={1}
												placeholder="Paste or type your document text here..."
												value={text}
												onChange={handleTextChange}
												disabled={uploading}
												fullWidth
												sx={{
													flexGrow: 1,
													"& .MuiOutlinedInput-root": {
														height: "100%",
														alignItems: "flex-start",
													},
												}}
											/>

											<Button
												variant="contained"
												onClick={handleTextSubmit}
												disabled={!text.trim() || uploading}
												fullWidth
												size="large"
												startIcon={
													uploading ? (
														<CircularProgress size={20} color="inherit" />
													) : (
														<CheckCircle />
													)
												}
												sx={{ py: 1.5 }}
											>
												{uploading ? "Processing..." : "Submit & Audit"}
											</Button>
										</Stack>
									</Paper>
								</Box>
							</Box>

							{error && (
								<Alert severity="error" sx={{ width: "100%", mt: 2 }}>
									{error}
								</Alert>
							)}

							{steps && (
								<Card
									sx={{
										width: "100%",
										mt: 3,
										background: "linear-gradient(135deg, #e0f7fa 0%, #80deea 100%)",
									}}
								>
									<CardContent
										sx={{
											cursor: "pointer",
										}}
										onClick={() => setStepsExpanded(!stepsExpanded)}
									>
										<Stack direction="row" justifyContent="space-between" alignItems="center">
											<Typography variant="h6" color="primary" fontWeight="bold">
												Audit Steps
											</Typography>
											<Button
												size="small"
												variant="text"
												sx={{ minWidth: "auto", p: 0.5 }}
											>
												{stepsExpanded ? <ExpandLess /> : <ExpandMore />}
											</Button>
										</Stack>
										{stepsExpanded && (
											<Box
												component="pre"
												sx={{
													mt: 2,
													backgroundColor: "#004d40",
													color: "#b2dfdb",
													padding: 2,
													borderRadius: 2,
													overflow: "auto",
													fontSize: "0.875rem",
													fontFamily: '"Consolas", "Monaco", "Courier New", monospace',
													maxHeight: "400px",
												}}
											>
												{steps.map((step, index) => `${index + 1}. ${step}`).join("\n")}
											</Box>
										)}
									</CardContent>
								</Card>
							)}

                            {extraction && (
                                <Card sx={{
                                        width: "100%",
                                        mt: 3,
                                        background: "linear-gradient(135deg, #e0f7fa 0%, #80deea 100%)",
                                    }}>
                                    <CardContent
                                        sx={{
                                            cursor: "pointer",
                                        }}
                                        onClick={() => setExtractionExpanded(!extractionExpanded)}
                                    >
                                        <Stack direction="row" justifyContent="space-between" alignItems="center">
                                            <Typography variant="h6" color="primary" fontWeight="bold">
                                                Document Metadata
                                            </Typography>
                                            <Button
                                                size="small"
                                                variant="text"
                                                sx={{ minWidth: "auto", p: 0.5 }}
                                            >
                                                {extractionExpanded ? <ExpandLess /> : <ExpandMore />}
                                            </Button>
                                        </Stack>
                                        {extractionExpanded && (
                                            <Box
                                                sx={{
                                                    mt: 2,
                                                    backgroundColor: "#004d40",
                                                    color: "#b2dfdb",
                                                    padding: 2,
                                                    borderRadius: 2,
                                                    overflow: "auto",
                                                    fontSize: "0.875rem",
                                                    fontFamily: '"Consolas", "Monaco", "Courier New", monospace',
                                                    maxHeight: "400px",
                                                }}
                                            >
                                                <pre>{JSON.stringify(extraction, null, 2)}</pre>
                                            </Box>
                                        )}
                                    </CardContent>
                                </Card>
                            )}

							{response?.issues && (
								<Stack 
                                    spacing={2} mt={2}
                                    sx={{width:"100%"}}
                                >
                                    <Typography variant="h6" color="primary" fontWeight="bold">
										Audit Results
									</Typography>
									{response.issues.map((issue: any, index: number) => (
										<Card key={index} variant="outlined">
											<CardContent>
												<Stack
													direction="row"
													justifyContent="space-between"
													alignItems="center"
												>
													<Typography variant="subtitle1" fontWeight="bold">
														{issue.type}
													</Typography>
													<Chip
														label={issue.severity.toUpperCase()}
														color={
															issue.severity === "high"
																? "error"
																: issue.severity === "medium"
																? "warning"
																: "success"
														}
														size="small"
													/>
												</Stack>
												<Typography variant="body2" mt={1}>
													{issue.description}
												</Typography>
												<Typography variant="body2" mt={1} color="text.secondary">
													Suggestion: {issue.suggestion}
												</Typography>
											</CardContent>
										</Card>
									))}
								</Stack>
							)}
						</Stack>
					</Paper>
				</Container>
			</Box>
		</ThemeProvider>
	);
}

export default App;
