<?php
    $data = ["prefered_name" => "Martim Videira"];

    require 'vendor/autoload.php';
    use Symfony\Component\Yaml\Yaml;

    $yaml = file_get_contents("./../experience.yaml");

    $dir    = './imgs/icons';
    $icons = array_diff(scandir($dir), array('..', '.'));
    $nIcons = count($icons);

    $data = Yaml::parse($yaml);
    $parseDown = new Parsedown();

    function windowHeader($level,$title,$icon) {
        $title_el = "<h" . $level . ">" . $title . "</h". $level . ">" ; ?>

          <div class="window-header">
              <div class= "window-title" >
              <img class="window-icon"src="./imgs/icons/<?= $icon ?>">
              <h2><?= $title ?></h2>
              </div>
              <?= windowControls() ?>
          </div>
    <?php }
    function windowControls(){ ?>

            <div class="window-controls">
                <img src="./imgs/window-controls-minimize.png"/>
                <img src="./imgs/window-controls-maximize.png"/>
                <img src="./imgs/window-controls-close.png"/>
            </div>
    <?php }
    function windowHeaderBase($title_el) {
        ?>
        <div class="window-header">
            <?= $title_el ?>
            <?= windowControls() ?>
        </div>
    <?php } 

    function folder($title,$items) {       global $icons;global $nIcons; ?>

      <article class ="window folder">
          <?php windowHeader(2,$title, "explorer.exe_14_252-3.png") ?>
          <div class="window-folder">
            <div class="window-folder-container">
          <?php  foreach ($items  as $item) { ?>
                  <div class="icon">
                <img src= "./imgs/icons/<?= $icons[rand(0,$nIcons-1)] ?>"/>
                  <span><?= $item ?>  </span>
                  </div>
          <?php } ?>
          </div>
          </div>

      </article>
     <?php }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> <?php echo $data["prefered_name"] ?>'s CV </title>   
    <link rel="stylesheet" href="./styles.css"/>
</head>
<body>
    <article class="window about-me">
    <?= windowHeader(1,"About Me",  "nusrmgr.cpl_14_200-6.png") ?>
    <div class="about-me">
      <div class="about-me-content">
        <section id="education" >
            <h2>Education</h2>
            <p><?= $data["education"]["degree"] ?> from the <?= $data["education"]["university"] ?> <?= $data["education"]["from"]["begin"] ?> to <?= $data["education"]["from"]["end"] ?> </p>
        </section>
        <section id="languages">
            <h2>Languages</h2>
            <ul>
            <?php  foreach ($data["languages"] as $language) { ?>
                    <li>
                    <div class="icon">
                        <img src="./imgs/<?=$language["l"]?>.svg"> 
                    <span><?= $language["level"]?>  </span>
                    </div>
            </li>
            <?php } ?>
            </ul>
        </section>
        <section>
        <h2>Links</h2>
        <nav>
            <ul>
                <li>
                <img src = "./imgs/icons/console.dll_14_1-5.png"/>
                <a href="<?= $data["github"]["link"]?>"><?= $data["github"]["display"]?></a>
                </li>
                <li>
                  <img src = "./imgs/icons/ahui.exe_14_2006-3.png"/>
                  <a href="<?= $data["linkedin"]["link"]?>"><?= $data["linkedin"]["display"]?></a></li>
                <li>
                <img src = "./imgs/icons/msoeres.dll_14_2-6.png"/>
                  <a href="mailto:<?= $data["email"]?>"><?= $data["email"]?></a></li>
            </ul>
        </nav>
            </section>
      </div>
    <div id="user-profile">
      <img src="./imgs/user-icon.webp">
      <h1><?= $data["prefered_name"]?></h1>
    </div>
    </div>
    </article>
    <article class="window">
        <?= windowHeader(2,"Experience","shell32.dll_14_22-8.png")?> </h3>
        <section id="experience-container">
        <?php  foreach ($data["experience"] as $experience) { ?>
                <article class="experience">
                <img src= "./imgs/icons/<?= $icons[rand(0,$nIcons-1)] ?>"/>
                <div class="experience-content">
                <h3> <?= $experience["position"]?> </h3>
                <div> <?= $parseDown->text($experience["description"])?> </div>
        </div>
          </article>
        <?php } ?>
        </section>
      
        </article>
    <section id="projects">
        <h2>Projects</h2>
        <section id="projects-container">
        <?php  foreach ($data["projects"] as $project) { ?>
            <article class="window project">
            <?php  windowHeader(3,$project["name"],"shell32.dll_14_302-5.png")?> 
            <div> <?= $parseDown->text($project["description"])?> </div>
            <div class="project-technologies">
            <?php  foreach ($project["technologies"] as $technology) { ?>
                <div class="icon">
                <img src= "./imgs/icons/<?= $icons[rand(0,$nIcons-1)] ?>"/>
                <span><?= $technology ?>  </span>
                </div>
            <?php } ?>
            </div>
            </article>
        <?php } ?>
        </section>
    </section>
    <div class="folder-container">
    <?= folder("Programming Languages",$data["programming_languages"]) ?>
    <?= folder("Technologies",$data["technologies"]) ?>
    </div>
</body>
</html>