<?php

if (!file_exists(".htaccess") || !file_exists("config.php")) {
	echo '<p class="error">Project setup is not complete.<br />-&gt; <a href="install.php">Go to installation</a>?</p>';
}

?>
