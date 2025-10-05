# AI Service Testing Scripts

This directory contains connectivity and functionality tests for AI vision services.

## Setup

1. **Install dependencies**:
   ```bash
   hatch shell
   pip install openai anthropic python-dotenv
   ```

2. **Configure API keys**:
   ```bash
   # Copy example file
   cp .env.example .env
   
   # Edit .env and add your API keys
   # OpenAI: https://platform.openai.com/api-keys
   # Anthropic: https://console.anthropic.com/settings/keys
   ```

## Check Scripts

### OpenAI GPT-4o Vision

**Basic connectivity test**:
```bash
python tests/check_openai.py
```

**Vision analysis with image**:
```bash
python tests/check_openai.py /path/to/fridge-photo.jpg
```

**What it tests**:
- ✅ API key configuration
- ✅ Basic API connectivity
- ✅ Image analysis with food identification
- ✅ Structured output parsing

### Anthropic Claude Vision

**Basic connectivity test**:
```bash
python tests/check_anthropic.py
```

**Vision analysis with image**:
```bash
python tests/check_anthropic.py /path/to/fridge-photo.jpg
```

**What it tests**:
- ✅ API key configuration
- ✅ Basic API connectivity
- ✅ Image analysis with food identification
- ✅ Base64 image encoding

## Expected Output

### Successful Connection Test

```
============================================================
OpenAI Vision API Connectivity Test - FA-3
============================================================

Test 1: Basic API connectivity
------------------------------------------------------------
✅ OpenAI API connection successful: API connection successful

Test 2: Skipped (no image provided)
Usage: python check_openai.py <path-to-image>

============================================================
```

### Successful Vision Analysis

```
Test 2: Vision analysis
------------------------------------------------------------
Analyzing image: fridge.jpg
✅ OpenAI Vision analysis complete
Response: [
  {
    "item_name": "Greek Yogurt - Chobani",
    "quantity": 3,
    "confidence": 0.95,
    "is_leftover": false
  },
  {
    "item_name": "Milk - 2%",
    "quantity": 1,
    "confidence": 0.98,
    "is_leftover": false
  },
  ...
]
```

## Troubleshooting

### API Key Not Configured

```
❌ OpenAI API key not configured
Set OPENAI_API_KEY in .env file or environment
```

**Solution**: Add your API key to `.env` file:
```
OPENAI_API_KEY=sk-proj-YOUR_KEY_HERE
```

### Missing Dependencies

```
Error: Required package not installed: No module named 'openai'
Run: hatch shell, then pip install openai python-dotenv
```

**Solution**: Install dependencies:
```bash
hatch shell
pip install openai anthropic python-dotenv
```

### Image Not Found

```
❌ Image file not found: /path/to/image.jpg
```

**Solution**: Provide a valid image path:
```bash
python tests/check_openai.py ~/Pictures/fridge-photo.jpg
```

## Cost Estimates

**OpenAI GPT-4o**:
- Basic test: ~$0.0001 per test
- Vision analysis: ~$0.006 per image

**Anthropic Claude**:
- Basic test: ~$0.0002 per test
- Vision analysis: ~$0.008 per image

## Next Steps

After successful testing:

1. **FA-4**: Collect 10-15 test fridge photos
2. **FA-5**: Develop and refine prompts for better accuracy
3. **FA-7**: Run comparison between OpenAI and Anthropic on real images
4. **FA-10**: Integrate chosen service into main application

## See Also

- [AI Services Research](../docs/AI_SERVICES_RESEARCH.md) - Detailed comparison and recommendations
- [Implementation Guide](../implementation-guide.md) - Overall project architecture
- [Requirements](../requirements.md) - Project goals and phases
