#!/bin/bash

rm -rf /usr/local/bin/node /usr/local/bin/npm /usr/local/bin/npx /usr/local/bin/pm2 \
&& ln -s /www/server/nvm/versions/node/v*/bin/node /usr/local/bin/ \
&& ln -s /www/server/nvm/versions/node/v*/bin/npm /usr/local/bin/ \
&& ln -s /www/server/nvm/versions/node/v*/bin/npx /usr/local/bin/ \
&& ln -s /www/server/nvm/versions/node/v*/bin/pm2 /usr/local/bin/ \
&& node -v \
&& npm -v \
&& pm2 -v