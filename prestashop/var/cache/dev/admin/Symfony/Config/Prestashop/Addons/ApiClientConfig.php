<?php

namespace Symfony\Config\Prestashop\Addons;

use Symfony\Component\Config\Loader\ParamConfigurator;
use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class ApiClientConfig 
{
    private $ttl;
    private $verifySsl;
    private $_usedProperties = [];

    /**
     * @default 0
     * @param ParamConfigurator|int $value
     * @return $this
     */
    public function ttl($value): static
    {
        $this->_usedProperties['ttl'] = true;
        $this->ttl = $value;

        return $this;
    }

    /**
     * @default '/var/www/html/var/cache/dev/cacert.pem'
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function verifySsl($value): static
    {
        $this->_usedProperties['verifySsl'] = true;
        $this->verifySsl = $value;

        return $this;
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('ttl', $value)) {
            $this->_usedProperties['ttl'] = true;
            $this->ttl = $value['ttl'];
            unset($value['ttl']);
        }

        if (array_key_exists('verify_ssl', $value)) {
            $this->_usedProperties['verifySsl'] = true;
            $this->verifySsl = $value['verify_ssl'];
            unset($value['verify_ssl']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['ttl'])) {
            $output['ttl'] = $this->ttl;
        }
        if (isset($this->_usedProperties['verifySsl'])) {
            $output['verify_ssl'] = $this->verifySsl;
        }

        return $output;
    }

}
