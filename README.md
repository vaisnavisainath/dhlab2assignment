# Student Digital Humanities Exhibition Template

This template is a single, self-contained webpage for a student's **multiple Digital Humanities assignments**. You only need `index.html` to publish it on GitHub Pages—there are no installations, accounts beyond GitHub, or build tools required.

## Before publishing

1. Download or copy `index.html` into a new folder.
2. Open it in a text editor (for example, VS Code, Notepad, or GitHub's online editor).
3. Replace all text marked `[EDIT: ...]` with your own work.
4. Keep the six Student details fields in the stated order. Change only the Name value; the other five values are already set for this assignment.
5. Each `Assignment` block is a separate exhibit. Replace its title, abstract, and visible work. You can delete unused blocks, duplicate a block to add more, or rearrange them. The page automatically numbers the assignments and updates the “On this page” list when it opens.
6. Replace the GitHub repository link in every Assignment block with the repository for that project. The visible button opens the repository in a new tab.
7. Open `index.html` in a web browser to check your work.

## Publish with GitHub Pages

1. Sign in to [GitHub](https://github.com) and create a new **public** repository, for example `your-name-dh-project`.
2. Upload `index.html` to the top level of that repository. Its name must be exactly `index.html`.
3. In the repository, open **Settings** → **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select the `main` branch and the `/ (root)` folder, then click **Save**.
6. After GitHub finishes deploying (usually a few minutes), return to **Settings** → **Pages**. Copy the displayed site address and submit that link.

## Adding images or files

Create an `images` folder beside `index.html`, upload your image files there, and use paths like this in your page:

```html
<img src="images/my-image.jpg" alt="A concise description of the image">
```

Always add useful `alt` text and credit images, archives, data, and tools in “Sources and acknowledgements.”

## Responsive media

The template automatically resizes text, images, video, embeds, and the page layout for phones, tablets, desktop screens, high-zoom viewing, and print. For a wide video or interactive embed, wrap it in a `media-frame`:

```html
<div class="media-frame">
  <iframe src="https://example.com" title="Describe the embedded work"></iframe>
</div>
```

The page also follows a visitor’s light/dark-mode and reduced-motion preferences.

## Good publishing practice

- Use a clear project title and a brief abstract.
- Make each assignment visible on the page rather than only linking to a file.
- Check that every GitHub repository button leads to the correct assignment repository.
- Check that all links work on the deployed GitHub Pages site.
- Do not upload private information or material you do not have permission to share.
