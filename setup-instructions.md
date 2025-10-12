# Sample Configuration: Lilith Dystopia Gallery on Wix (Sim City / LA City / Netflix Style)

## 1. Wix Site Setup

### a. Create Your Wix Site
1. Go to [Wix.com](https://www.wix.com) and create an account.
2. Choose a template that fits a gallery or portfolio (try searching for “city”, “gallery”, or “portfolio”).
3. Name your site (e.g., "Lilith Dystopia: LA City Gallery").

### b. Add Wix CMS (Collections)
1. Go to the **Editor** > **Content Manager**.
2. Create a new collection called **“Dystopia Images”**.
   - Fields: Image, Title, Description, Tags, Location (set default to “Los Angeles” or allow multiple cities), Date Added.

## 2. Netflix-Style Gallery in Wix

1. Add a **Repeater** or **Gallery** element to your page.
2. Connect the repeater/gallery to your “Dystopia Images” collection.
3. Customize the layout to create a grid (use large thumbnails, overlay titles, “hover for description”—like Netflix).
4. Style the gallery with dark mode or neon colors for a dystopian aesthetic.

## 3. Automatic Updates with Amazon S3

### a. Store Images in Amazon S3
1. Create an [Amazon S3](https://aws.amazon.com/s3/) bucket (e.g., `lilith-dystopia-images`).
2. Upload your images. Set permissions for public read or restrict as needed.

### b. Automate Image Sync (Wix + S3)
Wix does not natively support S3 sync, but you can automate this with [Zapier](https://zapier.com/) or [Make.com](https://www.make.com/) as follows:

1. Set up a Zapier or Make scenario:
    - **Trigger**: New file added to Amazon S3 bucket.
    - **Action**: Create a new item in Wix CMS collection, filling in the image URL (from S3), title, etc.
2. Link your AWS and Wix accounts as per Zapier/Make instructions.
3. Map S3 image fields to Wix CMS fields.

#### Example Zapier Workflow:
- **Trigger**: Amazon S3 — New File in Bucket
- **Action**: Wix Automations — Create Item in CMS Collection

> If you need to use only Wix, manually upload images to the CMS, or use Wix’s own Media Manager.

## 4. Add LA City Tagging

- Use the “Location” field in your CMS.
- Default to “Los Angeles” or let users/curators add city tags.
- Display the city as a badge or filter in the gallery.

## 5. Final Touches

- Add a search/filter bar for tags and city.
- Use Wix’s built-in SEO tools to optimize for “Lilith Dystopia”, “LA City”, etc.
- Set up automatic publishing if using Zapier/Make.

---

## Example CMS Collection Entry

| Image (URL) | Title                | Description          | Tags         | Location    | Date Added |
|-------------|----------------------|----------------------|--------------|-------------|------------|
| (S3 URL)    | Neon Skyline         | Futuristic LA view   | neon, night  | Los Angeles | 2025-10-12 |
| (S3 URL)    | Dystopian Downtown   | Sim City inspired    | simcity, art | Los Angeles | 2025-10-12 |

---

## Optional: Netflix-Style Overlay

- Use Wix repeater/gallery settings to show overlay info on hover.
- Add animated transitions for a streaming-service feel.

---

## References

- [Wix Content Manager](https://support.wix.com/en/article/about-the-content-manager)
- [Zapier: Connect Wix & Amazon S3](https://zapier.com/apps/wix/integrations/amazon-s3)
- [Wix Gallery Customization](https://support.wix.com/en/article/customizing-your-gallery)

---

**You now have a code-free, auto-updating, Netflix-style Sim City/LA gallery for Lilith Dystopia images!**