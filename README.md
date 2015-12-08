# MinecraftPatcher
A small python script that downloads a .zip from a web server to update a minecraft modpack to distribute to others easily, the best base launcher to use is FTB or ATLauncher.

The ZIP requires a hierarchy like below (make sure only those 3 folders and whats meant to be in them is there nothing else): 
  <ul>
    <li>Modpack.zip</li>
      <ul>
        <li>config</li>
          <ul><li>configs.ext</li></ul>
        <li>mods</li>
          <ul><li>mods.ext</li></ul>
        <li>jarmods</li>
          <ul><li>jar.mods</li></ul>
      </ul>
  </ul>

It also requires a file outside the zip caled svn.txt, this acts as the version control. Generally the best thing to type is:
<code>
  Version: 1.0
</code>

Then update it when ever you push a new ZIP to the web server.

CopyRight Desgyz
